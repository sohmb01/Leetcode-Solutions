# Problem ID: 735
# Title: Asteroid Collision
# Runtime: 6 ms

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for ast in asteroids:
            while st and st[-1] > 0 and ast < 0:
                if st[-1] < abs(ast):
                    a = st.pop()
                    continue
                elif st[-1] == abs(ast):
                    st.pop()
                break
            else:
                st.append(ast)
                    
        return st