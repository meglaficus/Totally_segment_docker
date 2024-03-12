FROM pytorch/pytorch:2.2.1-cuda11.8-cudnn8-runtime
# FROM rocm/pytorch

RUN apt update
RUN apt install git -y

RUN pip install nnunetv2==2.2.1 tqdm
RUN pip install git+https://github.com/wasserth/TotalSegmentator.git
RUN totalseg_download_weights
COPY totally_segment.py /home/app/
# RUN mkdir -p /home/app/TotalSeg