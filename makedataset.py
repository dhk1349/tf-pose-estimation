#there should be one person in the sample

def transfer(sample):
    #input: list of human class objects
    #each human obj is dict 
    #
    result=[]
    for i in sample[0].body_parts:
        result.append([sample[0].body_parts[i].part_idx, sample[0].body_parts[i].x, sample[0].body_parts[i].y])

    return result
