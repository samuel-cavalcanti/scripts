#! /bin/bash


download_images(){

    page="https://files.passeidireto.com/a562d0c6-23c8-499c-95aa-d85360615ceb/bg"

    for ((i=1; i<=180;i++))
    do 
        page_i=$page$i".png"
        wget $page_i

    done

    for i in a b c d e f;
    do 
    page_i=$page"17"$i".png"
    wget $page_i  
    
    done 

}

rename_files(){
    file="bg"
    end_file=".png"

    for ((i=1;i<=179;i++))
    do 
        current_file=$file$i$end_file
        mv $current_file $i$end_file
    done

    n=180

    for i in a b c d e f
    do  
        current_file=$file"17"$i$end_file
        mv $current_file $n$end_file
        n=$((n+1))
        
    done

    mv $file"180"$end_file $n$end_file

}

dir="images/"
mkdir $dir
cd $dir

download_images

rename_files

cd ..

$python ./py_pdf.py $dir 1 186  "solidos.pdf"


rm -rf $dir