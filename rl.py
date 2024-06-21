import fitz
import json

community = ["OC", "BC", "MBC&DNC", "BCM", "SC", "ST", "SCA"]


def chunk(lines):
  li = []
  a = 0
  for i in range(0, len(lines)):
    if lines[i].startswith(" "):
      c = i + 1
      li.append(lines[a:c])
      a = c
  return li


def get_ranks(file_name):
  ranks = []

  pages = fitz.open(file_name)
  for page in pages:
    lines = page.get_text().split("\n")
    line = chunk(lines[11:-2])

    for data in line:

      rank = data[0]
      app_no = data[1]
      roll_no = data[2]
      name = data[3]
      comm = data[4]
      if comm not in community:
        comm = data[3].split(" ")[-1]
        name = " ".join(data[3].split(" ")[:-1])
        if comm not in community:
          for c in community:
            if c in comm:
              name = name + " " + comm[:-len(c)]
              comm = c
      mark = data[-1].strip()
      comm_rank = data[-2] if comm != "OC" else ""

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


def rl(rlist, file_name):
  ranks = get_ranks(rlist)
  with open(file_name, "w") as f:
    json.dump(ranks, f, indent=4)