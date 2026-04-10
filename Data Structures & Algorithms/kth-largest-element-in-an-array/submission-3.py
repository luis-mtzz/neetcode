class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # same max_heapify we wrote
        def max_heapify(A, i, heap_size):
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i

                if left < heap_size and A[left] > A[largest]:
                    largest = left
                if right < heap_size and A[right] > A[largest]:
                    largest = right

                if largest == i:
                    break

                A[i], A[largest] = A[largest], A[i]
                i = largest

        # same build_max_heap we wrote
        def build_max_heap(A):
            for i in range(len(A) // 2 - 1, -1, -1):
                max_heapify(A, i, len(A))

        # build the heap
        build_max_heap(nums)

        # extract the max k times
        heap_size = len(nums)
        for _ in range(k - 1):
            # swap root (max) with last element
            nums[0], nums[heap_size - 1] = nums[heap_size - 1], nums[0]
            heap_size -= 1
            # fix the heap
            max_heapify(nums, 0, heap_size)

        return nums[0]
         