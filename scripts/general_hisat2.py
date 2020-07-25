# coding=UTF-8
# 目的：从NCBI的数据库批量化下载sra数据
# 1. read srr accession number file; 2. 根据下载的sccession file 读取SRR文件下载地址；3. 根据SRR下载地址下载SRR文件；4 保存SRR文件；5. 批量化处理成fastq文件

import sys
acc_file =  sys.argv[1]
ref = sys.argv[2]
fq_dir = sys.argv[3]
with open (acc_file) as acc_file_handle:
    for line in acc_file_handle:
        # 直接print line的话会有换行，所以需要提前用rstrip去掉换行符
        line = line.rstrip()
        ele = line.split("\t")
        # print (ele)
        cmd_str = "hisat2 -x {ref} -U  {fq_dir}/{SRR}/{SRR}.fastq |samtools view -bS - |samtools sort - -o {sample_real_name}.sorted.bam \n samtools index {sample_real_name}.sorted.bam".format (ref = ref, fq_dir = fq_dir, SRR = ele[0], sample_real_name = ele[1])
        print(cmd_str)
