from collections import defaultdict

def canFinish(courses: int, prerequisites: list[list[int]])->bool:

    graph = defaultdict(list)

    for course , prereq in prerequisites:
        print(course ,"and" ,prereq )
        graph[course].append(prereq)


    return True 

def main():
    courses = 2
    prerequisites = [[1,0],[1,2],[2,3]]
    print(canFinish(courses, prerequisites))

if __name__ == "__main__":
    main()