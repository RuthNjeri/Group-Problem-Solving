#https://leetcode.com/problems/simplify-path/

def simplify_path(path)
    
    canonical_path = []
    directories = path.split('/')

    for dir in directories
        if dir == ".."
            canonical_path.pop
        elsif dir == "."
            next
        else
            canonical_path << dir if !dir.empty?
        end
    end
    "/#{canonical_path.join('/')}" 
end
