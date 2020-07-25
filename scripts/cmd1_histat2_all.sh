hisat2 -x /home/yxq/桌面/data/ref/yeast_ref -U  /home/yxq/桌面/data/RNA-seq/SRR1916152/SRR1916152.fastq |samtools view -bS - |samtools sort - -o EV_3.sorted.bam 
 samtools index EV_3.sorted.bam
hisat2 -x /home/yxq/桌面/data/ref/yeast_ref -U  /home/yxq/桌面/data/RNA-seq/SRR1916153/SRR1916153.fastq |samtools view -bS - |samtools sort - -o EV_4.sorted.bam 
 samtools index EV_4.sorted.bam
# hisat2 -x /home/yxq/桌面/data/ref/yeast_ref -U  /home/yxq/桌面/data/RNA-seq/SRR1916154/SRR1916154.fastq |samtools view -bS - |samtools sort - -o DNMT3B_2.sorted.bam 
# samtools index DNMT3B_2.sorted.bam
hisat2 -x /home/yxq/桌面/data/ref/yeast_ref -U  /home/yxq/桌面/data/RNA-seq/SRR1916155/SRR1916155.fastq |samtools view -bS - |samtools sort - -o DNMT3B_3.sorted.bam 
 samtools index DNMT3B_3.sorted.bam
hisat2 -x /home/yxq/桌面/data/ref/yeast_ref -U  /home/yxq/桌面/data/RNA-seq/SRR1916156/SRR1916156.fastq |samtools view -bS - |samtools sort - -o DNMT3B_4.sorted.bam 
 samtools index DNMT3B_4.sorted.bam
