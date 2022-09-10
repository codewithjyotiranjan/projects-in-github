def searching(sentence1,sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")

    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score+=1
    return score

if __name__ == '__main__':
    # print(searching("This is good","Python is good"))
    sentences = ["Python is a good","this is snake","harry is a good","harry is a good boy","subscribe to code with harry"]
    query = input("please enter the query string")
    score = [searching(query,sentence) for sentence in sentences]
    # print(score)
    sortedsentscore = [sentscore for sentscore in sorted(zip(score,sentences),reverse=True) if sentscore[0]!=0]
    # print(sortedsentscore)
    print(f"{len(sortedsentscore)} results found")
    for score ,item in sortedsentscore:
        print(f"\"{item}\"")


