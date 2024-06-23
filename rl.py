import fitz
import json

community = ["OC", "BC", "MBC&DNC", "BCM", "SC", "ST", "SCA"]


def chunk(lines, sp, af, df):
  li = []
  a = 0
  for i in range(0, len(lines)):
    spl = sp
    if lines[i].startswith(" "):
      if af:
        if lines[i + df] in community:

          if lines[i + df] == "OC":
            spl = spl - 1
      c = i + spl
      li.append(lines[a:c])
      a = c
  return li


def get_ranks(file_name, map):
  ranks = []

  pages = fitz.open(file_name)
  for page in pages:
    lines = page.get_text().split("\n")
    sp = map["split"]
    af = bool(map["af"])
    if map["index"]["mark"] < map["index"]["comm"]:
      df = map["index"]["comm"] - map["index"]["mark"]
    else:

      df = 0
    line = chunk(lines[map["list"]["start"]:map["list"]["end"]], sp, af, df)

    for data in line:
      rank = data[map["index"]["rank"]]

      app_no = data[map["index"]["app_no"]]
      roll_no = data[map["index"]["roll_no"]]
      name = data[map["index"]["name"]]
      comm = data[map["index"]["comm"]]

      if comm not in community:
        name = " ".join(comm.split(" ")[:-1])
        comm = name.split(" ")[-1]

        if comm not in community:

          for c in community:
            if c in comm:
              name = name + " " + comm[:-len(c)]
              comm = c

      mark = data[map["index"]["mark"]].strip()
      if not mark.isdigit():

        continue





      if comm != "OC":
        comm_rank = data[map["index"]["comm_rank"]]
      else:
        comm_rank = ""

      ranks.append({
          "rank": rank,
          "app_no": app_no,
          "roll_no": roll_no,
          # name not stored to protect student privacy
          # "name": name,
          "comm": comm,
          "mark": mark,
          "comm_rank": comm_rank
      })
  return ranks


def rl(rlist, file_name, map):
  with open(map, "r") as v:
    ranks = get_ranks(rlist, json.load(v))
  with open(file_name, "w") as f:
    json.dump(ranks, f, indent=4)
