class MyCircularQueue {
    public int[] queue;
    public int index;   
    public int capacity, front, rear;
    public MyCircularQueue(int k) {
        queue = new int[k];
        index = 0;
        capacity = k;
        front = -1;
        rear = -1;  
    }
    
    public boolean enQueue(int value) {
        if(isFull()){
            return false;
        }
        if(front == -1){
            front = 0;
            
        }
        rear = (rear + 1) % capacity;
        queue[rear] = value;
        return true;
    }
    
    public boolean deQueue() {
        if(isEmpty()){
            return false;
        }
        else if(front == rear){
            front = -1;
            rear = -1;
            return true;
        }
        front = (front+1) % capacity;
        return true;
    }
    
    public int Front() {
        if (isEmpty()){
            return -1;
        }
        else{
            return queue[front];
        }
    }
    
    public int Rear() {
        if (isEmpty()){
            return -1;
            
        }
        return queue[rear];
        
    }
    
    public boolean isEmpty() {
        return front == -1;
    }
    
    public boolean isFull() {
        if ((rear + 1) % capacity == front){
            return true;
        }
        else if(front == 0 && rear == capacity - 1){
            return true;
        }
        else{return false;}
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */