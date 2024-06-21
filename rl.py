import fitz
import json

community = ["OC", "BC", "MBC&DNC", "BCM", "SC", "ST", "SCA"]


def chunk(lines,sp):
  li = []
  a = 0
  for i in range(0, len(lines)):
    if lines[i].startswith(" "):
      c = i + sp
      li.append(lines[a:c])
      a = c
  return li


def get_ranks(file_name,vec):
  ranks = []

  pages = fitz.open(file_name)
  for page in pages:
    lines = page.get_text().split("\n")

    line = chunk(lines[vec["list"]["start"]:vec["list"]["end"]],vec["split"])
    

    for data in line:
      rank = data[vec["index"]["rank"]]

      app_no = data[vec["index"]["app_no"]]
      roll_no = data[vec["index"]["roll_no"]]
      name = data[vec["index"]["name"]]
      comm = data[vec["index"]["comm"]]

      if comm not in community:
        name = " ".join(comm.split(" ")[:-1])
        comm = name.split(" ")[-1]

        if comm not in community:
  
          for c in community:
            if c in comm:
              name = name + " " + comm[:-len(c)]
              comm = c
   

      mark = data[vec["index"]["mark"]].strip()
      comm_rank = data[vec["index"]["comm_rank"]] if comm != "OC" else ""

      ranks.append({
          "rank": rank,
          "app_no": app_no,
          "roll_no": roll_no,
          "name": name,
          "comm": comm,
          "mark": mark,
          "comm_rank": comm_rank
      })
  return ranks


def rl(rlist, file_name,vec):
  with open(vec, "r") as v:
    ranks = get_ranks(rlist,json.load(v))
  with open(file_name, "w") as f:
    json.dump(ranks, f, indent=4)