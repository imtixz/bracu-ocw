export default function Topbar() {
  return (
    <div className="h-[64px] bg-neutral-800 flex items-center p-6">
        <p className="text-white cursor-pointer">
          <span className="font-mono text-lg">BRACU</span>{" "}
          <span className="font-mono text-lg">OpenCourseWare</span>{" "}
          <span className="text-xs font-mono">[unofficial]</span>
        </p>
    </div>
  )
}
