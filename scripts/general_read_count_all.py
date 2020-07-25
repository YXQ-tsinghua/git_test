# coding=UTF-8
# 目的:根据比对的结果利用htseq_count计算counts数目
# 

import sys
 =  sys.argv[1]
with open (acc_file) as acc_file_handle:
    for line in acc_file_handle:
        # 直接print line的话会有换行，所以需要提前用rstrip去掉换行符
        line = line.rstrip()
        ele = line.split("\t")
        # print (ele)
        cmd_str = "hisat2 -x {ref} -U  {fq_dir}/{SRR}/{SRR}.fastq |samtools view -bS - |samtools sort - -o {sample_real_name}.sorted.bam \n samtools index {sample_real_name}.sorted.bam".format (ref = ref, fq_dir = fq_dir, SRR = ele[0], sample_real_name = ele[1])
        print(cmd_str)
