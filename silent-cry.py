#!/usr/bin/python3
#! -*- coding: utf-8 -*-
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% Date: Decembre 20, 2017 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%% Weather: It's always cool in the lab %%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%% Health: Overweight %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%% Caffeine: 12975 mg %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%% Hacked: All the things %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# By :     Hirokazo Nagata
# Fb : Hirokazo Nagata
# Github : https://github.com/CyB3rC0ntRol3
# Gmail :   ziadabouelfarah2@gmail.com1

import os,time
#This lib i made it and it have some encryption logarithm IF YOu wanT to developed you can add others logarithm in the endecode file
import endecode
import arts

os.system('clear')

print(arts.art1())
time.sleep(2)
os.system('clear')

print(arts.art1())
print(arts.art2())
print(" ")
print("\033[95m1- \033[91mEncryption\033[97m")
print("\033[95m2- \033[92mDecode\033[97m")
print(" ")
Ibtissam = input('\033[93m+>>')
#################################################################################
##################################################################################
if Ibtissam == '1':
    print('Chose one of this ENCRYPT logarithm to work with it :')
    print ('')
    print('1-AES')
    print('2-XOR')
    print('3-Base64 [!]No Key Hir[!]')
    print('4-Base32 [!]No Key Hir[!]')
    print('5-Base16 [!]No Key Hir[!]')
    salma =input("\033[93m+>>" )
##############################################################################################
    if salma == str(1) or salma == "1":
        print("Do you want For me to random a key [y/n] :")
        anser = input(">>> ")
        if anser == "n":
            key= input("\033[95m[?] \033[97mEnter your \033[97m\033[91mKEY \033[97m:\033[93m")
            pass
        else:
            key = endecode.random_line('keys.txt')
            print("Your Key Is : "+key)
        file_location=input("\033[95m[?] \033[97mDrag the \033[91mfile\033[97m:\033[93m")
        endecode.encodeAES(key,file_location)
        print("Your File was Encrypt by SUCCESS ;) ")
################################################################################
    if salma == str(2) or salma == "2":
        print("Do you want For me to random a key [y/n] :")
        anser = input(">>> ")
        if anser == "n":
            key = input("\033[95m[?] \033[97mEnter your \033[97m\033[91mKEY \033[97m:\033[93m")
            pass 
        else:
            key = endecode.random_line('keys.txt')
            print("Your Key Is : "+ key)
        file_location = input("\033[95m[?] \033[97mDrag the \033[91mfile\033[97m:\033[93m")
        endecode.encodeXOR(key, file_location)
        print("Your File was Encrypt by SUCCESS ;) ")
#################################################################################
    if salma == str(3) or salma == "3":
        file_location = input("\033[95m[?] \033[97mDrag the \033[91mfile\033[97m:\033[93m")
        endecode.encodeBASE64(file_location)
        print("Your File was Encrypt by SUCCESS ;) ")
#################################################################################
    if salma == str(4) or salma == "4":
        file_location = input("\033[95m[?] \033[97mDrag the \033[91mfile\033[97m:\033[93m")
        endecode.encodeBASE64(file_location)
        print("Your File was Encrypt by SUCCESS ;) ")

#################################################################################
    if salma == str(5) or salma == "5":
        file_location = input("\033[95m[?] \033[97mDrag the \033[91mfile\033[97m:\033[93m")
        endecode.encodeBASE64(file_location)
        print("Your File was Encrypt by SUCCESS ;) ")
#####################################################################################


if Ibtissam == '2':
    print('Chose one of this DECRYPT logarithm to work with it :')
    print ('')
    print('1-AES')
    print('2-XOR')
    print('3-Base64 [!]No Key Hir[!]')
    print('4-Base32 [!]No Key Hir[!]')
    print('5-Base16 [!]No Key Hir[!]')
    salma =input("\033[93m+>>" )
##############################################################################################
    if salma == str(1) or salma == "1":
        key= input("\033[95m[?] \033[97mEnter your \033[97m\033[91mKEY \033[97m:\033[93m")
        file_location=input("\033[95m[?] \033[97mDrag the \033[91mfile\033[97m:\033[93m")
        endecode.decodeAES(key,file_location)
        print("Your File was Decrypt by SUCCESS ;) ")
################################################################################
    if salma == str(2) or salma == "2":
        key = input("\033[95m[?] \033[97mEnter your \033[97m\033[91mKEY \033[97m:\033[93m")
        file_location = input("\033[95m[?] \033[97mDrag the \033[91mfile\033[97m:\033[93m")
        endecode.decodeXOR(key, file_location)
        print("Your File was Decrypt by SUCCESS ;) ")
#################################################################################
    if salma == str(3) or salma == "3":
        file_location = input("\033[95m[?] \033[97mDrag the \033[91mfile\033[97m:\033[93m")
        endecode.decodeBASE64(file_location)
        print("Your File was Decrypt by SUCCESS ;) ")
#################################################################################
    if salma == str(4) or salma == "4":
        file_location = input("\033[95m[?] \033[97mDrag the \033[91mfile\033[97m:\033[93m")
        endecode.decodeBASE32(file_location)
        print("Your File was Decrypt by SUCCESS ;) ")

#################################################################################
    if salma == str(5) or salma == "5":
        file_location = input("\033[95m[?] \033[97mDrag the \033[91mfile\033[97m:\033[93m")
        endecode.decodeBASE16(file_location)
        print("Your File was Decrypt by SUCCESS ;) ")
#####################################################################################