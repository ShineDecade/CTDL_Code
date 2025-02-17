using DataStructures

mutable struct Stack
    elements::Deque{Any}
end

Stack() = new(Deque{Any}())

function push!(s::Stack, item)
    push!(s.elements, item)
    println("Đã thêm '$item' vào ngăn xếp.")
end

function pop!(s::Stack)
    if !isempty(s.elements)
        item = pop!(s.elements)
        println("Đã lấy '$item' ra khỏi ngăn xếp.")
        return item
    else
        println("Ngăn xếp trống!")
        return nothing
    end
end

function peek(s::Stack)
    if !isempty(s.elements)
        return last(s.elements)
    else
        println("Ngăn xếp trống!")
        return nothing
    end
end

function is_empty(s::Stack)
    return isempty(s.elements)
end

function print_stack(s::Stack)
    println("Ngăn xếp (đỉnh đến đáy): ", reverse(s.elements))
end

function main()
    stack = Stack()

    push!(stack, "Sách A")
    push!(stack, "Sách B")
    push!(stack, "Sách C")

    print_stack(stack)

    top_item = peek(stack)
    println("Phần tử ở đỉnh ngăn xếp: ", top_item)

    pop!(stack)
    print_stack(stack)

    println("Ngăn xếp có trống không? ", is_empty(stack) ? "Có" : "Không")
end

main()