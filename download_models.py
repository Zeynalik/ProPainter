import urllib.request

urls = [
    "https://github.com/sczhou/ProPainter/releases/download/v0.1.0/ProPainter.pth",
    "https://github.com/sczhou/ProPainter/releases/download/v0.1.0/recurrent_flow_completion.pth",
    "https://github.com/sczhou/ProPainter/releases/download/v0.1.0/raft-things.pth",
    "https://github.com/sczhou/ProPainter/releases/download/v0.1.0/i3d_rgb_imagenet.pt"
]

weights_folder = "weights/"

for url in urls:
    file_name = url.split("/")[-1]
    print(f"Downloading {file_name}...")
    urllib.request.urlretrieve(url, weights_folder + file_name)
    print(f"Downloaded {file_name} successfully!")


Included plugins:

1.  NppExport v0.4
2.  Converter v4.6
3.  Mime Tool v3.1


Updater (Installer only):

* WinGUp (for Notepad++) v5.3
