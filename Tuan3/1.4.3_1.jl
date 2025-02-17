mutable struct Stack{T}
    elements::Vector{T}
end

Stack{T}() where {T} = new(Vector{T}())

function push!(s::Stack{T}, item::T) where {T}
    push!(s.elements, item)
    println("Đã thêm '$item' vào ngăn xếp.")
end

function pop!(s::Stack{T}) where {T}
    if !isempty(s.elements)
        item = pop!(s.elements)
        println("Đã lấy '$item' ra khỏi ngăn xếp.")
        return item
    else
        println("Ngăn xếp trống!")
        return nothing
    end
end

function peek(s::Stack{T}) where {T}
    if !isempty(s.elements)
        return s.elements[end]
    else
        throw(ArgumentError("Ngăn xếp trống!"))
    end
end

function is_empty(s::Stack)
    return isempty(s.elements)
end

function display(s::Stack)
    println("Ngăn xếp (đỉnh đến đáy): ", s.elements)
end

function main()
    stack = Stack{String}()  # Khai báo ngăn xếp lưu trữ các chuỗi

    push!(stack, "Sách A")
    push!(stack, "Sách B")
    push!(stack, "Sách C")

    display(stack)

    top_item = peek(stack)
    println("Phần tử ở đỉnh ngăn xếp: ", top_item)

    pop!(stack)
    display(stack)

    println("Ngăn xếp có trống không? ", is_empty(stack) ? "Có" : "Không")
end

main()