#
# Image hash for calculating some hash value for given image
# 
#   to use this file type
# 
#   pip install ImageHash
#

from PIL import Image
import imagehash

def myhash(file):
  hash = imagehash.average_hash(Image.open(file))
  return hash

def myhashimg(img):
  hash = imagehash.average_hash(img)
  return hash


if __name__ == "__main__":
    import sys
    hash = myhash(sys.argv[1])
    print(sys.argv[1], hash)

    hash1 = myhashimg (Image.open(sys.argv[1]))
    print(sys.argv[1], hash1)

