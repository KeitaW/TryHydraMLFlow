import os
from omegaconf import DictConfig
import hydra

@hydra.main(config_path='conf/config.yaml')
def show_config(cfg):
    print(cfg.pretty())

@hydra.main(config_path='conf/config.yaml')
def check_path(cfg: DictConfig) -> None:
    print(f'Current working directory: {os.getcwd()}')
    print(f'Orig working directory : {hydra.utils.get_original_cwd()}')
    print(f'to_absolute_path("foo") : {hydra.utils.to_absolute_path("foo")}')
    print(f'to_absolute_path("/foo") : {hydra.utils.to_absolute_path("/foo")}')

if __name__ == "__main__":
    show_config()
    check_path()