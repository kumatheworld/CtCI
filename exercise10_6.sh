input_file=$1
output_file=$2

lines_per_file=10000000
prefix=${input_file}.split_x

split -l ${lines_per_file} ${input_file} ${prefix}

for file in ${prefix}*; do
    sort -o ${file} ${file}
done

sort --merge -o ${output_file} ${prefix}*

for file in ${prefix}*; do
    rm $file
done
