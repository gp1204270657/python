#coding=utf-8
import sys,os
import openpyxl
import json
base_path=os.getcwd()
sys.path.append(base_path)
from Util.handle_json import read_json

def get_header():
    header=read_json("/Config/header.json")
    return header
    
