For part 2 I change the input to one long list by using the following commands:
 
    for f in {1..3}; do awk -v col="$f" '{print $col}' < input >> single_column_list; done

