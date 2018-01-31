#!usr/bin/python3
#! -*- coding: utf-8 -*-

from Crypto.Cipher import *
import base64,random,os,hashlib,time

#####################################################################################################
# Hir I made diffrent Encode and decodde logarthme So if you want to dev just add  new logarthme    #
#####################################################################################################


######################################################################################################################
###########################################       Encoding          ##################################################
######################################################################################################################

def encodeAES(key,dir):
    if '.cry' not in dir:
        files = open(dir,"rb")
        think = files.read()
        files.close()
        think = str(think)
        print(think)
        os.system('clear')
        print("encoding data of the file ...")
        time.sleep(3)
        ########################################################################
        BLOCK_SIZE = 32
        PADDING = '{'
        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
        EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
        secret = hashlib.md5(str(key).encode('utf-8')).hexdigest()
        cipher = AES.new(secret)
        encoded = EncodeAES(cipher, think)
        ###########################################################################
        print(encoded)
        encoded = str(encoded)
        time.sleep(3)
        print('writing in you file ...')
        os.remove(dir)
        newfile = open(dir + '.cry',"w")
        newfile.write(encoded)
        newfile.close()
    else:
        print("The File is already encrypt")


def encodeXOR(key,dir):
    if '.cry' not in dir:
        files = open(dir,"rb")
        think = files.read()
        files.close()
        think = str(think)
        print(think)
        os.system('clear')
        print("encoding data of the file ...")
        time.sleep(3)
        ########################################################################
        secret = hashlib.md5(key).hexdigest()
        cipher = XOR.new(secret)
        encoded = base64.b64encode(cipher.encrypt(read))
        ###########################################################################
        encoded = str(encoded)
        print(encoded)
        time.sleep(3)
        print('writing in you file ...')
        os.remove(dir)
        newfile = open(dir + '.cry',"w")
        newfile.write(encoded)
        newfile.close()
    else:
        print("The File is already encrypt")

def encodeBASE64(dir):
    if '.cry' not in dir:
        files = open(dir,"rb")
        think = files.read()
        files.close()
        think = str(think)
        print(think)
        os.system('clear')
        print("encoding data of the file ...")
        time.sleep(3)
        os.system('clear')
        ########################################################################
        encoded = base64.b64encode(think)
        ###########################################################################
        encoded = str(encoded)
        print(encoded)
        time.sleep(3)
        print('writing in you file ...')
        os.remove(dir)
        newfile = open(dir + '.cry',"w")
        newfile.write(encoded)
        newfile.close()
    else:
        print("The File is already encrypt")

def encodeBASE32(dir):
    if '.cry' not in dir:
        files = open(dir,"rb")
        think = files.read()
        files.close()
        think = str(think)
        print(think)
        os.system('clear')
        print("encoding data of the file ...")
        time.sleep(3)
        ########################################################################
        encoded = base64.b32encode(think)
        ###########################################################################
        print(encoded)
        encoded = str(encoded)
        time.sleep(3)
        print('writing in you file ...')
        os.remove(dir)
        newfile = open(dir + '.cry',"w")
        newfile.write(encoded)
        newfile.close()
    else:
        print("The File is already encrypt")

def encodeBASE16(dir):
    if '.cry' not in dir:
        files = open(dir,"rb")
        think = files.read()
        files.close()
        think = str(think)
        print(think)
        os.system('clear')
        print("encoding data of the file ...")
        time.sleep(3)
        ########################################################################
        encoded = base64.b16encode(think)
        ###########################################################################
        encoded = str(encoded)
        print(encoded)
        time.sleep(3)
        print('writing in you file ...')
        os.remove(dir)
        newfile = open(dir + '.cry',"w")
        newfile.write(encoded)
        newfile.close()
    else:
        print("The File is already encrypt")

######################################################################################################################
###########################################       Decoding          ##################################################
######################################################################################################################


def decodeAES(key,dir):
    if '.cry' in dir:
        files = open(dir,"rb")
        think = files.read()
        files.close()
        think = str(think)
        print(think)
        os.system('clear')
        print('Decoding your data File....')
        ############################################################################
        PADDING = '{'
        DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
        secret = hashlib.md5(key).hexdigest()
        cipher = AES.new(secret)
        decoded = DecodeAES(cipher, think)
        ###########################################################################
        decoded = str(decoded)
        print(decoded)
        name = dir.replace('.cry',"")
        os.remove(dir)
        print('writing in to your file...')
        newfile = open(name,"w")
        newfile.write(decoded)
        newfile.close()
    else:
        print("The File is not encrypt to Decrypt")

def decode_XOR(key,dir):
    if '.cry' in dir:
        files = open(dir,"rb")
        think = files.read()
        files.close()
        think = str(think)
        print(think)
        os.system('clear')
        print('Decoding your data File....')
        ############################################################################
        secret = hashlib.md5(key).hexdigest()
        cipher = XOR.new(secret)
        encoded = cipher.decrypt(base64.b64decode(read))
        ###########################################################################
        decoded = str(decoded)
        print(decoded)
        name = dir.replace('.cry',"")
        os.remove(dir)
        print('writing in to your file...')
        newfile = open(name,"w")
        newfile.write(decoded)
        newfile.close()
    else:
        print("The File is not encrypt to Decrypt")

def decode_BASE64(dir):
    if '.cry' in dir:
        files = open(dir,"rb")
        think = files.read()
        files.close()
        think = str(think)
        print(think)
        os.system('clear')
        print('Decoding your data File....')
        ############################################################################
        encoded = base64.b64decode(think)
        ###########################################################################
        decoded = str(decoded)
        print(decoded)
        name = dir.replace('.cry',"")
        os.remove(dir)
        print('writing in to your file...')
        newfile = open(name,"w")
        newfile.write(decoded)
        newfile.close()
    else:
        print("The File is not encrypt to Decrypt")

def decode_BASE32(dir):
    if '.cry' in dir:
        files = open(dir,"rb")
        think = files.read()
        files.close()
        think = str(think)
        print(think)
        os.system('clear')
        print('Decoding your data File....')
        ############################################################################
        encoded = base64.b32decode(think)
        ###########################################################################
        decoded = str(decoded)
        print(decoded)
        name = dir.replace('.cry',"")
        os.remove(dir)
        print('writing in to your file...')
        newfile = open(name,"w")
        newfile.write(decoded)
        newfile.close()
    else:
        print("The File is not encrypt to Decrypt")

def decode_BASE16(dir):
    if '.cry' in dir:
        files = open(dir,"rb")
        think = files.read()
        files.close()
        think = str(think)
        print(think)
        os.system('clear')
        print('Decoding your data File....')
        ############################################################################
        encoded = base64.b16decode(think)
        ###########################################################################
        decoded = str(decoded)
        print(decoded)
        name = dir.replace('.cry',"")
        os.remove(dir)
        print('writing in to your file...')
        newfile = open(name,"w")
        newfile.write(decoded)
        newfile.close()
    else:
        print("The File is not encrypt to Decrypt")


###################################################################################################
############################# This For help   #####################################################
###################################################################################################

def random_line(dir):
    lines = open(dir).read().splitlines()
    myline = random.choice(lines)
    return myline
