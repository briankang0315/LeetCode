function twoSum(nums: number[], target: number): number[] {
 
    for (let i = 0; i < nums.length; i++){
        for (let j = i+1; j < nums.length; j++){
            let k = nums[i] + nums[j];
            
            if (k == target){
                const x: number[] = [i, j];
                
                return x
            }
        }
    }
};