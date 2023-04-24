import hashlib
import subprocess
from model import user
from passlib.hash import sha512_crypt
from dataclasses import dataclass
import crypt

@dataclass
class UserAccount:
    def Login(self, User: user) -> bool:
        username = User.name
        password = User.password
        sudo_password="42316421"
        command = f"echo {sudo_password} | sudo -S cat /etc/shadow | grep {username}"
        output = subprocess.check_output(command, shell=True)
        if output:
            hashed_password = output.decode().strip().split(":")[1]
            if crypt.crypt(password, hashed_password) == hashed_password:
                return True
            else:
                return False

    def zipfile(self,User:user)->bool:
        username=User.name
        password=User.password
        hostname='rike-VirtualBox'
        command = f"sshpass -p '{password}' ssh -o StrictHostKeyChecking=no {username}@{hostname} 'cd ~ && tar czvf - .' | cat > /tmp/homedir.zip"
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            raise Exception("Failed to create zip file")
        else:
            return True
    
    