from main import init, run, close, table

init("maindb")

new = table("test", ["name", "age", "date"], ["INT"])
new.create()

close()
