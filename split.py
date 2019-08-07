import os
from config import *

ind_keys = ["BookmarkTitle", "BookmarkLevel", "BookmarkPageNumber"]
bookmarkkeys = set(ind_keys + ["BookmarkBegin"])


def serializar(d):
    print(str(d))


for tomo in tomos_suffixes:
    indfilename = os.path.join(tomos_dir, ind_file_prefix + tomo + ".info")
    tiffs_dir = os.path.join(tomos_dir, tiffs_subdir_prefix + tomo)

    state = 0  # 0: no bookmark 1: in bookmark
    num_pages = -1
    bookmarkdata = {x: None for x in ind_keys}
    output = []
    with open(indfilename) as fin:
        i = 0
        for row in fin:
            rows = row.strip()
            if len(row) < 1:
                continue
            if ":" in rows and rows.split(":")[0] == "NumberOfPages":
                num_pages = int(rows.split(":")[1])
            # Ya terminamos de revisar un doc
            if state == 1 and all([x is not None for x in bookmarkdata.values()]):
                # print(serializar(bookmarkdata))
                output.append([bookmarkdata["BookmarkTitle"], bookmarkdata["BookmarkPageNumber"]])
                for k in bookmarkdata.keys():
                    bookmarkdata[k] = None
            if rows == "BookmarkBegin":
                state = 1
                continue
            rowsp = rows.split(":")
            if rowsp[0] not in bookmarkkeys:
                state = 0
                continue
            if len(rowsp) == 1:
                print("\n!!!", rows)
                break
            bookmarkdata[rowsp[0]] = rowsp[1].strip()
            if rowsp[0] == "BookmarkTitle":
                bookmarkdata[rowsp[0]] = "\"" + bookmarkdata[rowsp[0]] + "\""
            if rowsp[0] == "BookmarkPageNumber":
                bookmarkdata[rowsp[0]] = int(bookmarkdata[rowsp[0]])

    # add end of document
    output.sort(key=lambda x: x[1])
    for i, re in enumerate(output[:-1]):
        output[i].append(int(output[i + 1][1]) - 1)
    output[-1].append(num_pages)

    #output = [x for x in output if int(x[1]) < x[2]]

    outfn = os.path.join(tomos_dir, output_prefix + tomo + ".csv")
    with open(outfn, "wt") as fout:
        for i, d in enumerate(output):
            start = d[1]
            end = d[2]
            if end < start:
                end = start
            title = d[0]
            docname = "doc_" + tomo + "_" + str(i)
            for imn in range(start, end + 1):
                imagename = "TOMO_" + tomo + "_" + str(imn) + ".tiff"
                fout.write(";".join([imagename, docname, title]) + "\n")
