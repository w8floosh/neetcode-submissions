func maxArea(heights []int) int {
    maxa := 0

    for i,j := 0, len(heights)-1; i < j; {
        minh := min(heights[i],heights[j])
        area := minh * (j-i)
        if area > maxa {
            maxa = area
        }
        
        if heights[i] == minh {
            i = i+1
        } else {
            j = j-1
        }
    }

    return maxa
}


