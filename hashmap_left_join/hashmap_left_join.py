def left_join(table,table_2):
    '''
    This function make a LEFT JOINs two hashmaps into a single data structure then return it.
    '''
    all_keys_values_table=table.keys_values()
    all_keys_values_table_2=table_2.keys_values()
    for i in range(len(all_keys_values_table)):
        for j in range(len(all_keys_values_table_2)):
            if all_keys_values_table[i][0]==all_keys_values_table_2[j][0]:
                all_keys_values_table[i].append(all_keys_values_table_2[j][1])
        if len(all_keys_values_table[i])<3 :
            all_keys_values_table[i].append(None)

    return all_keys_values_table
    


if __name__ == "__main__":
    from hash_table import HashTable
    table_1=HashTable()
    table_1.set("diligent","employed")
    table_1.set("fond","enamored")
    table_1.set("guide","usher")
    table_1.set("outfit","garb")
    table_1.set("wrath","anger")

    table_2=HashTable()
    table_2.set("diligent","idle")
    table_2.set("fond","averse")
    table_2.set("wrath","delight")
    table_2.set("guide","follow")
    table_2.set("flow","jam")
    print(left_join(table_1,table_2))