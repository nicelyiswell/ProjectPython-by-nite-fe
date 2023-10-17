def main():
    # Number of people
    N = int(input())
    
    # First person's favorites
    common_favorites = set(input().split())
    
    # Intersecting the favorites with every next person
    for _ in range(N-1):
        next_person_favorites = set(input().split())
        common_favorites &= next_person_favorites
    
    # Sorting in lexicographical order
    sorted_common_favorites = sorted(common_favorites)
    
    # Output
    if sorted_common_favorites:
        print(' '.join(sorted_common_favorites))
    else:
        print("Nothing")

if __name__ == "__main__":
    main()
