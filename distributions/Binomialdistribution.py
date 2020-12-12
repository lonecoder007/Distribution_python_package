import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials
    
    
    TODO: Fill out all TODOs in the functions below
            
    """
    
    def __init__(self, prob=.5, n=20):
        
        self.p=prob
        self.n=n
        Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())    
    
    def calculate_mean(self):
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """     
        self.mean=self.n*self.p
        return self.mean


    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        self.stdev=math.sqrt(self.n*self.p*(1-self.p))
        return self.stdev
        
        
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """        
        
        # TODO: The read_data_file() from the Generaldistribution class can read in a data
        #       file. Because the Binomaildistribution class inherits from the Generaldistribution class,
        #       you don't need to re-write this method. However,  the method
        #       doesn't update the mean or standard deviation of
        #       a distribution. Hence you are going to write a method that calculates n, p, mean and
        #       standard deviation from a data set and then updates the n, p, mean and stdev attributes.
        #       Assume that the data is a list of zeros and ones like [0 1 0 1 1 0 1]. 
        #
        #       Write code that: 
        #           updates the n attribute of the binomial distribution
        #           updates the p value of the binomial distribution by calculating the
        #               number of positive trials divided by the total trials
        #           updates the mean attribute
        #           updates the standard deviation attribute
        #
        #       Hint: You can use the calculate_mean() and calculate_stdev() methods
        #           defined previously.
        self.n=len(self.data)
        self.p=sum(self.data)/len(self.data)
        self.mean=self.calculate_mean()
        self.stdev=self.calculate_stdev()
        return self.p , self.n
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
            
        # TODO: Use the matplotlib package to plot a bar chart of the data
        #       The x-axis should have the value zero or one
        #       The y-axis should have the count of results for each case
        plt.bar([0,1],[(1-self.p)*n,self.p*self.n])
        plt.label("Bar Chart")
        plt.xlabel("Outcome")
        plt.ylabel('Count')   
        
    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        a=math.factorial(self.n)/(math.factorial(k)*math.factorial(self.n-k))
        b=(self.p**k)*(1-self.p)**(self.n-k)
        return a*b
             

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
    
        # TODO: Use a bar chart to plot the probability density function from
        # k = 0 to k = n
        x=[]
        y=[]
        for i in (self.n+1):
            x.append(i)
            y.append(self.pdf(i))
        
        plt.bar(x,y)
        plt.label("Population Density Function")
        plt.xlabel("Outcome")
        plt.ylable('Probability')
        return x,y
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        # TODO: Define addition for two binomial distributions. Assume that the
        # p values of the two distributions are the same. The formula for 
        # summing two binomial distributions with different p values is more complicated,
        # so you are only expected to implement the case for two distributions with equal p.
        
        # the try, except statement above will raise an exception if the p values are not equal
        
        # Hint: You need to instantiate a new binomial object with the correct n, p, 
        #   mean and standard deviation values. The __add__ method should return this
        #   new binomial object.
        
        #   When adding two binomial distributions, the p value remains the same
        #   The new n value is the sum of the n values of the two distributions.
                
        result=Binomial()
        result.n=self.n+other.n
        result.p=self.p
        result.calculate_mean()
        result.calculate_stdev()
        return result
    
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        
        # TODO: Define the representation method so that the output looks like
        #       mean 5, standard deviation 4.5, p .8, n 20
        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean,self.stdev,self.p,self.n)
