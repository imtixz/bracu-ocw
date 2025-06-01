function App() {

  return (
    <div className="bg-stone-100">
      <div className="h-[64px] bg-neutral-800 flex items-center p-6">
        <p className="text-white cursor-pointer">
          <span className="font-mono text-lg">BRACU</span>{" "}
          <span className="font-mono text-lg">OpenCourseWare</span>{" "}
          <span className="text-xs font-mono">[unofficial]</span>
        </p>
      </div>
      <div className="min-h-[calc(100vh-64px)] h-full">
        <div className="flex flex-col items-center my-12 gap-y-3">
          <p className="text-4xl">Explore OpenCourseWare</p>
          <p className="text-lg">Search for courses, materials & teaching resources</p>
          <input className="min-w-[512px] h-[32px] px-4 py-5 border border-gray-300 rounded mt-5 shadow-md" />
        </div>
      
        <div className="flex flex-col sm:flex-row mx-12">
          <div className="border-t-2 w-[384px]">filters</div>
          <div className="w-full bg-stone-200 flex flex-col gap-y-4 py-4">
           <div className="bg-white flex flex-col mx-8 px-5 py-6 rounded shadow-md">
              <p className="text-sm font-bold text-blue-800">CSE330 | Spring'25</p>
              <p className="text-lg font-bold">Numerical Methods</p>
              <div className="flex flex-row gap-x-3 mt-3">
                <p className="py-0.5 px-3 bg-gray-200 text-sm rounded-xs">SDS</p>
                <p className="py-0.5 px-3 bg-gray-200 text-sm rounded-xs">Lecture Notes</p>
                <p className="py-0.5 px-3 bg-gray-200 text-sm rounded-xs">Video</p>
              </div>
            </div>
            <div className="bg-white flex flex-col mx-8 px-5 py-6 rounded shadow-md">
              <p className="text-sm font-bold text-blue-800">CSE330 | Summer'25</p>
              <p className="text-lg font-bold">Numerical Methods</p>
              <div className="flex flex-row gap-x-3 mt-3">
                <p className="py-0.5 px-3 bg-gray-200 text-sm rounded-xs">SDS</p>
                <p className="py-0.5 px-3 bg-gray-200 text-sm rounded-xs">Lecture Notes</p>
                <p className="py-0.5 px-3 bg-gray-200 text-sm rounded-xs">Video</p>
              </div>
            </div>
          </div>
        </div>

        </div>
    </div>
  )
}

export default App
