
import cv2


# print(w,h)

# filepath = 'runs\detect\exp\labels\im (1911).txt'


def details(path,w,h):
    stone_dict = {}
    stones_dict = {}

    with open(path) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            # print("Line {}: {}".format(cnt, line.strip()))
            line_text=line.strip()
            X_CENTER=float(line_text.split(" ", 5)[1])*w
            Y_CENTER =float(line_text.split(" ", 5)[2])*h
            WIDTH =float(line_text.split(" ", 5)[3])*w
            HEIGHT=float(line_text.split(" ", 5)[4])*h
            print(X_CENTER,Y_CENTER,WIDTH,HEIGHT)
            line = fp.readline()
            
                
            stone_name = 'stone{}'.format(cnt)

            stone_dict = {}

            #stone_dict['contour'] = cnt.reshape((-1,2)).tolist()
            stone_dict['area'] = HEIGHT*WIDTH
            stone_dict['length'] = HEIGHT
            stone_dict['width'] = WIDTH
            stones_dict[stone_name] = stone_dict

            cnt += 1

    return cnt,stones_dict


# print(stones_dict)
