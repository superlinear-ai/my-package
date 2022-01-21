# My Package

A Python package that demos Poetry Cookiecutter.

## Using

To serve this package, run `docker-compose up app`.

## Contributing

<details>
<summary>Setup: once per device</summary>

1. [Generate an SSH key and add it to your authentication agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), and [add the SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
1. [Install Docker Desktop](https://www.docker.com/get-started).
1. [Configure Docker and Docker Compose to use the BuildKit build system](https://pythonspeed.com/articles/docker-buildkit/):
    ```bash
    # bash
    echo "export DOCKER_BUILDKIT=1" >> ~/.bash_profile
    echo "export COMPOSE_DOCKER_CLI_BUILD=1" >> ~/.bash_profile

    # fish
    echo "set --export DOCKER_BUILDKIT 1" >> ~/.config/fish/config.fish
    echo "set --export COMPOSE_DOCKER_CLI_BUILD 1" >> ~/.config/fish/config.fish
    
    # zsh
    echo "export DOCKER_BUILDKIT=1" >> ~/.zshenv
    echo "export COMPOSE_DOCKER_CLI_BUILD=1" >> ~/.zshenv
    ```
1. [Install VS Code](https://code.visualstudio.com/) and [VS Code's Remote-Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Alternatively, install [PyCharm](https://www.jetbrains.com/pycharm/download/).
1. _Optional:_ [Install FiraCode Nerd Font](https://www.nerdfonts.com/font-downloads) with `brew tap homebrew/cask-fonts && brew install --cask font-fira-code-nerd-font` and [configure VS Code](https://github.com/tonsky/FiraCode/wiki/VS-Code-Instructions) or [configure PyCharm](https://github.com/tonsky/FiraCode/wiki/Intellij-products-instructions) to use `'FiraCode Nerd Font'`.

</details>

<details open>
<summary>Setup: once per project</summary>

1. Clone this repository.
2. Open the cloned repository in VS Code and run <kbd>⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd> > _Remote-Containers: Reopen in Container_ to start a [Development Container](https://code.visualstudio.com/docs/remote/containers). Alternatively, open the cloned repository in PyCharm and [configure Docker Compose as a remote interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote).
3. Run `poe install` in the development environment to create the Python environment and register [pre-commit](https://pre-commit.com/). This happens automatically in VS Code, but needs to be done manually in PyCharm.

</details>

<details open>
<summary>Developing</summary>

- This project's development environment is managed by [Docker Compose](https://docs.docker.com/compose/) with `docker-compose.yml` and `Dockerfile`, while its dependencies are specified with [Poetry](https://github.com/python-poetry/poetry) in `pyproject.toml` and `poetry.lock`.
- This project follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen).
- Every commit is linted by [pre-commit](https://pre-commit.com/) with the linters listed in `.pre-commit-config.yaml`. All linters are configured in `pyproject.toml`.
- Run `poe` from within the development environment to print a list of [Poe the Poet](https://github.com/nat-n/poethepoet) tasks available to run on this project.
- Run `poetry add {package}` from within the development environment to install a run time dependency and add it to `poetry.lock`. Add `--group dev` if you only need the package for local development, or `--group test` if you only need the package for linting or testing.
- Run `poetry update` from within the development environment to upgrade all dependencies to the latest versions allowed by `pyproject.toml`.

</details>
