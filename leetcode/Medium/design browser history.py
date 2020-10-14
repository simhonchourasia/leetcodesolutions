# https://leetcode.com/problems/design-browser-history/

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.curr = 0
        self.length = 1
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.history = self.history[:self.curr+1]
        self.history.append(url)
        self.length = len(self.history)
        self.curr = self.length - 1
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.curr-steps<0:
            self.curr = 0
        else:
            self.curr -= steps
        return self.history[self.curr]
        
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.curr+steps >= self.length:
            self.curr = self.length-1
        else:
            self.curr += steps
        return self.history[self.curr]
        
