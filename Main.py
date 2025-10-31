import argparse
import os
import PyBass.bass as b
import os.path as p
import time
from os import _exit as exit
def GetFoundedMusic(musicname : str):
    if(p.exists(musicname)):
        return True
    else:
        return False

def SetGitDownloadAndCreateFolder(git_websitesrccode : str, env_name, foldername):
    os.environ[env_name] = foldername
    os.system("mkdir {}".format(os.environ[env_name]))
    print("Please Set VS 2022 Pro in System Environment aka conhost because this script only works if VS 2022 already set in System Environment!!!")
    os.system("git clone {} --recurse-submodules {}".format(git_websitesrccode, os.environ[env_name]))
    if(p.exists(os.environ[env_name] + "\\msvc\\mono.sln")):
        print("Successfully Founded mono.sln!!! Trying to run Visual Studio 2022 Pro or Any of Edition...")
        time.sleep(4)
        os.system("start devenv.exe {}".format(os.environ[env_name] + "\\msvc\\mono.sln"))
        print("Successfully Launched!!!")
        exit(3312)
    else:
        print("Failed to Found mono.sln... Please Try Again or Run this as Administrator!!!")
        time.sleep(4)
        exit(221)

def PlayMusic(filename):
    if(b.BASS_INIT(device=-1, freq=44100, flags=0, win=0, dsguid=0)):
        b.BASS_START()
        stream_file = b.BASS_StreamCreateFile(mem=0, filename=str(filename).encode("utf-8"), offset=0, length=0, flags=0x4)
        b.BASS_ChannelPlay(stream_file, False)
    else:
        print("Failed to Init Un4Seen Bass!!!")
        time.sleep(10)
        exit(443)

def Main():
    if GetFoundedMusic("MrRobotMainMenu.mp3"):
        PlayMusic("MrRobotMainMenu.mp3")
        SetGitDownloadAndCreateFolder("https://github.com/Unity-Technologies/mono.git", "MONO_UNITY3DFOLDER_SRCCODE", "MonoFromUnity3D\\mono")
    else:
        exit(4435)

if __name__ == "__main__":
    Main()

