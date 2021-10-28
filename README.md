# A utility to convert yaml to flat file 

This is a utility developed in python to convert a yaml to flat file. In this case we will be using an fstab entry file which is in yaml format.

## How to use
a) Clone to your local - `git clone https://github.com/govindkailas/util.git && cd util`

b) Install the python pre-req package - `pip install requirements.txt` 

   If `pip` is not installed follow https://pip.pypa.io/en/stable/installation/ to install pip first 

c) Once the above steps are done, we are good to convert the yaml format file to fstab entry file - `python3 yamlutil.py <path_to_yaml_which_contain_fstab>`

Note: Script will not overwrite your fstab entry, it will simply create a output file in the same folder.


## Testing
```bash
python3 yamlutil.py fstab.yaml 
Output file for fstab generated!, check out fstab-output.txt

$ cat fstab-output.txt 
/dev/sda1 /boot  xfs   defaults 0 0
/dev/sda2 /  ext4   defaults 0 0
/dev/sdb1 /var/lib/postgresql  ext4 10%  defaults 0 0
192.168.4.5 /home /var/nfs/home nfs  noexec,nosuid  0 0
/dev/sda7 /mnt/Windows  ntfs-3g  quiet,defaults,locale=en_US.utf8,umask=0,noexec  0 0
```
## Warning
Before replacing your fstab with the script output, make sure to verify it and proceed only if its good. Wrong entries can screw up your linux machine!! 

