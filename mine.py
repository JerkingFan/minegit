import minecraft_launcher_lib
import subprocess

version = "1.12.1"
# Установка последней версии Minecraft
minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory='.mnlauncher')

# Получение команды для запуска Minecraft
options = {
    "username": "JerkingFan",
    "uuid": "",
    "token": ""
}

# Запуск Minecraft
subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory='.mnlauncher', options=options))

