class BorderedSection:
    def __init__(self, title):
        self.title = title
        
    def __enter__(self):
        self.line = f"=== {self.title} ==="
        print(self.line)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('=' * len(self.line))
        # return False
        
        
        
with BorderedSection("Results"):
    print("Score: 95")
    print("Grade: A")
