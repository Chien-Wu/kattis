"https://open.kattis.com/problems/towering"

raw_input = input().split()
boxes = [int(i) for i in raw_input]
tower1_heights = boxes[6]
tower2_heights = boxes[7]
boxes = boxes[:6]
for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        for k in range(i+2, len(boxes)):
            if boxes[i] + boxes[j] + boxes[k] == tower1_heights:
                if boxes[i] == boxes[j] or boxes[j] == boxes[k] or boxes[i] == boxes[k]:
                    continue
                else:
                    tower1 = [boxes[i], boxes[j], boxes[k]]
                    tower2 = [boxes[l] for l in range(len(boxes)) if l not in [i, j, k]]
                    break
tower1.sort(reverse=True)
tower2.sort(reverse=True)
print(tower1[0],tower1[1],tower1[2],tower2[0],tower2[1],tower2[2])