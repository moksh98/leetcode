class ProductOfNumbers {
    
    List<Integer> stream;
    
    public ProductOfNumbers() {
        stream = new ArrayList<>(){{add(1);}};
    }
    
    public void add(int num) {
        if(num > 0) {
            stream.add(stream.get(stream.size()-1)*num);
        }
        else {
            stream = new ArrayList<>(){{add(1);}};
        }
    }
    
    public int getProduct(int k) {
        return k < stream.size() ? stream.get(stream.size()-1)/stream.get(stream.size()-1-k) : 0;
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */