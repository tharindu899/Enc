"""Small smoke test for add_subtitles helper.

Usage (PowerShell):
python .\scripts\add_subs_test.py .\input.mp4 .\subs.srt .\output.mkv embed

"""
import asyncio
import sys

from bot.workers.encoders.encode import Encoder


async def main():
    if len(sys.argv) < 5:
        print("Usage: add_subs_test.py <input> <subtitle> <output> <mode: embed|burn>")
        return
    infile = sys.argv[1]
    sfile = sys.argv[2]
    outfile = sys.argv[3]
    mode = sys.argv[4]
    ok, out = await Encoder.add_subs(infile, outfile, sfile, mode=mode)
    print("Success:", ok)
    print(out)


if __name__ == "__main__":
    asyncio.run(main())
