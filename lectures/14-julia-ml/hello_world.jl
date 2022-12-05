msg = "Hello World"
if length(ARGS) > 0
    msg = msg * " & $(first(ARGS))!"
else
    msg = msg * "!"
end

println(msg)
