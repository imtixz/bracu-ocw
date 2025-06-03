interface TagProps {
  name: string
}

export default function Tag({name}: TagProps) {
  return (
    <p className="py-0.5 px-3 bg-gray-200 text-sm rounded-xs cursor-pointer">{name}</p>
  )
}
