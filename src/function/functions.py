#Copyright 2018 UNIST under XAI Project supported by Ministry of Science and ICT, Korea

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

#   https://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

import os
import scipy.misc as scm
import nibabel as nib

def make_project_dir(project_dir):
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
        os.makedirs(os.path.join(project_dir, 'models'))
        os.makedirs(os.path.join(project_dir, 'result'))
        os.makedirs(os.path.join(project_dir, 'result_test'))

def get_image(img_path):
    img = scm.imread(img_path)/255. - 0.5
    img = img[..., ::-1]  # rgb to bgr
    return img


def inverse_image(img):
    img = (img + 0.5) * 255.
    img[img > 255] = 255
    img[img < 0] = 0
    img = img[..., ::-1] # bgr to rgb
    return img

def save_as_nii(vol, aff, save_dir):
    for i in range(len(vol)):
        img = nib.Nifti1Image(dataobj=vol[i,...], affine=aff)
        nib.save(img,'{}_{}.nii'.format(save_dir,i))
    print("MRI file saved..!")
    return
