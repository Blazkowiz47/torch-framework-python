template: str = '''"""
Main training file.
calls the train pipeline with configs.
"""
import argparse
import datetime

import numpy as np
import torch
from torch.nn import CrossEntropyLoss
from torch.optim import AdamW
from torchmetrics import Accuracy
from tqdm import tqdm
import yaml
# Incase you use wandb uncomment following line
# import wandb

from models  import get_model 
from cdatasets import get_dataset 
from utils import logger, set_seeds, initialise_dirs


parser = argparse.ArgumentParser(
    description="Training Config",
    add_help=True,
)

parser.add_argument(
    "-m",
    "--model",
    default="sample",
    type=str,
    help="Model name.",
)

parser.add_argument(
    "-c",
    "--config",
    default="configs/train.yml",
    type=str,
    help="Train config file.",
)

parser.add_argument(
    "-d",
    "--datset",
    default="sample",
    type=str,
    help="""
    Give a single dataset name or multiple datasets to chain together.
    eg: -d datset1 
    """,
)

parser.add_argument(
    "--epochs",
    default=None,
    type=int,
    help="Override number of epochs fetch from the config file.",
)

parser.add_argument(
    "--batch-size",
    default=32,
    type=int,
    help="Override batch-size fetched from the config file.",
)

parser.add_argument(
    "--wandb-run-name",
    type=str,
    default=None,
    help="Give a wandb-run-name if you use wandb.",
)

parser.add_argument(
    "--validate-after-epochs",
    type=int,
    default=None,
    help="Override validate after epochs fetched from the config file.",
)

parser.add_argument(
    "--learning-rate",
    type=float,
    default=None,
    help="Override learning rate fetched from the config file.",
)

parser.add_argument(
    "-ckpt",
    "--continue-model",
    type=str,
    default=None,
    help="Load initial weights from partially/pretrained model.",
)

parser.add_argument(
    "--seed",
    type=int,
    default=2024,
    help="Set random seed value",
)

# You can add any additional arguments if you need here.


def main():
    """
    Wrapper for the driver.
    """
    args = parser.parse_args()
    logger.log = logger.get_logger(args.model + str(datetime.datetime.now()).replace(' ', '_'))
    log = logger.log

    with open(args.config, "r") as fp:
        config = yaml.safe_load(fp)


    initialise_dirs()
    set_seeds(args.seed or config["seed"])
    epochs = args.epochs or config["epochs"]
    validate_after_epochs = args.validate_after_epochs or config['validate_after_epochs'] 

    device = "cuda"     # You can change this to cpu.

    model = get_model(args.model, config).to(device)
    log.info(str(model))
    wrapper = get_dataset(args.dataset, config)
    
    trainds = wrapper.get_split("train")
    validationds = wrapper.get_split("validation")
    
    if args.continue_model:
        model.load_state_dict(torch.load(args.continue_model))

    criterion = CrossEntropyLoss().to(device)
    metric = Accuracy(task="multiclass", num_classes=wrapper.num_classes).to(device)
    optimizer = AdamW([p for p in model.parameters() if p.requires_grad], lr=config['lr'])

    for epoch in range(epochs):
        model.train()
        train_losses = [] 
        for image, label in tqdm(trainds, desc=f"Epoch {epoch +1}"):

            optimizer.zero_grad()
            image, label = image.to(device), label.to(device)

            preds = model(image)
            preds, label = preds.argmax(dim=1), label.argmax(dim=1)

            step_loss = criterion(preds, label)
            step_loss.backward()
            optimizer.step()

            metric.step(preds, label)
            train_losses.append(step_loss)

        log.info(f'Average train step loss: {np.mean(train_losses)}')
        log.info(f'Average train accuracy: {metric.compute()}')
        metric.reset() 

        if not epoch % validate_after_epochs:
            validation_losses = [] 
            model.eval()
            for image, label in tqdm(validationds, desc="Validation"):
                image, label = image.to(device), label.to(device)

                preds = model(image)
                preds, label = preds.argmax(dim=1), label.argmax(dim=1)
                step_loss = criterion(preds, label)
                
                metric.step(preds, label)
                validation_losses.append(step_loss)

            log.info(f'Average validation step loss: {np.mean(validation_losses)}')
            log.info(f'Average validation accuracy: {metric.compute()}')
        
       
        # add wandb logs if any

    # Uncomment following line if you use wandb
    # wandb_run_name = args.wandb_run_name
    # if wandb_run_name:
    #    wandb.init(
    #        # set the wandb project where this run will be logged
    #        project="<PROJECT-NAME>",
    #        name=wandb_run_name,
    #        config={
    #            **config,
    #            "dataset": args.dataset,
    #        },
    #    )

    for epoch in range(epochs):


    # if wandb_run_name:
    #     wandb.finish()


if __name__ == "__main__":
    main()
'''
