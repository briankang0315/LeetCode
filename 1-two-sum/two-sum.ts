function twoSum(nums: readonly number[], target: number): [number, number] {
  if (nums.length < 2) throw new Error("Input must have at least 2 numbers");

  const seen: { [key: number]: number } = {};

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    const prevIndex = seen[complement];

    if (prevIndex !== undefined) {
      return [prevIndex, i];
    }

    seen[nums[i]] = i;
  }

  throw new Error("No two sum solution found");
}
