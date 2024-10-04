#!/usr/bin/env python3
'''Lab 3 - Free Disk Space Function'''
# Author ID: ekoleci

import subprocess

def free_space():
    p = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    if error:
        return f'Error: {error.decode("utf-8").strip()}'
    lines = output.decode('utf-8').strip().split('\n')
    root_line = [line for line in lines if '/$' in line]
    
    if root_line:
        return root_line[0].split()[3].strip() 
    
    return 'Error: Unable to determine free space' 

if __name__ == '__main__':
    print(free_space())

