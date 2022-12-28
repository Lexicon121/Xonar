# Update tracking data from Xbox 360 Kinect
def video_frame_ready(frame):
    video = np.empty((480,640,4), np.uint8)
    frame.image.copy_bits(video.ctypes.data)
    return video

def depth_frame_ready(frame):
    depth = np.empty((424,512), np.uint16)
    frame.image.copy_bits(depth.ctypes.data)
    return depth

def skeleton_frame_ready(frame):
    skeletons = frame.SkeletonData
    for index, data in enumerate(skeletons):
        if data.eTrackingState == nui.SkeletonTrackingState.TRACKED:
            left_hand_pos = data.SkeletonPositions[JointId.HandLeft]
            x_kinect = left_hand_pos.x
            y_kinect = left_hand_pos.y
            z_kinect = left_hand_pos.z

kinect.skeleton_frame_ready += skeleton_frame_ready

# Update tracking data from HTC Vive Lighthouse
def update_vive_tracking():
    while True:
        poses_t = openvr.TrackedDevicePose_t * openvr.k_unMaxTrackedDeviceCount
        poses = poses_t()
        vive.compositor.getLastPoses(poses, openvr.k_unMaxTrackedDeviceCount)
        for nDevice in range(openvr.k_unMaxTrackedDeviceCount
