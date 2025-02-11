#!/usr/bin/env python3

import depthai as dai
import numpy as np
import sys
from pathlib import Path

# Connect Device
with dai.Device() as device:
    calibFile = str((Path(__file__).parent / Path(f"calib_{device.getMxId()}.json")).resolve().absolute())
    if len(sys.argv) > 1:
        calibFile = sys.argv[1]

    calibData = device.readCalibration()
    calibData.eepromToJsonFile(calibFile)

    M_rgb, width, height = calibData.getDefaultIntrinsics(dai.CameraBoardSocket.CAM_A)
    print("RGB Camera Default intrinsics...")
    print(M_rgb)
    print(f"Default fx (focal length x): {M_rgb[0][0]}")
    print(f"Default fy (focal length y): {M_rgb[1][1]}")
    print(f"Width: {width}")
    print(f"Height: {height}")

    if "OAK-1" in calibData.getEepromData().boardName or "BW1093OAK" in calibData.getEepromData().boardName:
        M_rgb = np.array(calibData.getCameraIntrinsics(dai.CameraBoardSocket.CAM_A, 1280, 720))
        print("\nRGB Camera resized intrinsics (1280x720)...")
        print(M_rgb)
        print(f"Resized fx: {M_rgb[0][0]}")
        print(f"Resized fy: {M_rgb[1][1]}")

        D_rgb = np.array(calibData.getDistortionCoefficients(dai.CameraBoardSocket.CAM_A))
        print("RGB Distortion Coefficients...")
        [print(name + ": " + value) for (name, value) in
         zip(["k1", "k2", "p1", "p2", "k3", "k4", "k5", "k6", "s1", "s2", "s3", "s4", "τx", "τy"],
             [str(data) for data in D_rgb])]

        print(f'RGB FOV {calibData.getFov(dai.CameraBoardSocket.CAM_A)}')

    else:
        M_rgb, width, height = calibData.getDefaultIntrinsics(dai.CameraBoardSocket.CAM_A)
        print("\nRGB Camera Default intrinsics...")
        print(M_rgb)
        print(f"Default fx: {M_rgb[0][0]}")
        print(f"Default fy: {M_rgb[1][1]}")
        
        # 1080p calculations 
        M_rgb = np.array(calibData.getCameraIntrinsics(dai.CameraBoardSocket.CAM_A, 1920, 1080))
        print("\nRGB Camera resized intrinsics (1920x1080)...")
        print(M_rgb)
        print(f"Resized fx: {M_rgb[0][0]}")
        print(f"Resized fy: {M_rgb[1][1]}")

        M_rgb = np.array(calibData.getCameraIntrinsics(dai.CameraBoardSocket.CAM_A, 3840, 2160))
        print("\nRGB Camera resized intrinsics (3840x2160)...")
        print(M_rgb)
        print(f"Resized fx: {M_rgb[0][0]}")
        print(f"Resized fy: {M_rgb[1][1]}")

        M_rgb = np.array(calibData.getCameraIntrinsics(dai.CameraBoardSocket.CAM_A, 4056, 3040))
        print("\nRGB Camera resized intrinsics (4056x3040)...")
        print(M_rgb)
        print(f"Resized fx: {M_rgb[0][0]}")
        print(f"Resized fy: {M_rgb[1][1]}")

        M_left, width, height = calibData.getDefaultIntrinsics(dai.CameraBoardSocket.CAM_B)
        print("LEFT Camera Default intrinsics...")
        print(M_left)
        print(width)
        print(height)

        M_left = np.array(calibData.getCameraIntrinsics(dai.CameraBoardSocket.CAM_B, 1280, 720))
        print("LEFT Camera resized intrinsics...  1280 x 720")
        print(M_left)

        M_right = np.array(calibData.getCameraIntrinsics(dai.CameraBoardSocket.CAM_C, 1280, 720))
        print("RIGHT Camera resized intrinsics... 1280 x 720")
        print(M_right)

        D_left = np.array(calibData.getDistortionCoefficients(dai.CameraBoardSocket.CAM_B))
        print("LEFT Distortion Coefficients...")
        [print(name+": "+value) for (name, value) in zip(["k1","k2","p1","p2","k3","k4","k5","k6","s1","s2","s3","s4","τx","τy"],[str(data) for data in D_left])]

        D_right = np.array(calibData.getDistortionCoefficients(dai.CameraBoardSocket.CAM_C))
        print("RIGHT Distortion Coefficients...")
        [print(name+": "+value) for (name, value) in zip(["k1","k2","p1","p2","k3","k4","k5","k6","s1","s2","s3","s4","τx","τy"],[str(data) for data in D_right])]

        print(f"RGB FOV {calibData.getFov(dai.CameraBoardSocket.CAM_A)}, Mono FOV {calibData.getFov(dai.CameraBoardSocket.CAM_B)}")

        R1 = np.array(calibData.getStereoLeftRectificationRotation())
        R2 = np.array(calibData.getStereoRightRectificationRotation())
        M_right = np.array(calibData.getCameraIntrinsics(calibData.getStereoRightCameraId(), 1280, 720))

        H_left = np.matmul(np.matmul(M_right, R1), np.linalg.inv(M_left))
        print("LEFT Camera stereo rectification matrix...")
        print(H_left)

        H_right = np.matmul(np.matmul(M_right, R1), np.linalg.inv(M_right))
        print("RIGHT Camera stereo rectification matrix...")
        print(H_right)

        lr_extrinsics = np.array(calibData.getCameraExtrinsics(dai.CameraBoardSocket.CAM_B, dai.CameraBoardSocket.CAM_C))
        print("Transformation matrix of where left Camera is W.R.T right Camera's optical center")
        print(lr_extrinsics)

        l_rgb_extrinsics = np.array(calibData.getCameraExtrinsics(dai.CameraBoardSocket.CAM_B, dai.CameraBoardSocket.CAM_A))
        print("Transformation matrix of where left Camera is W.R.T RGB Camera's optical center")
        print(l_rgb_extrinsics)