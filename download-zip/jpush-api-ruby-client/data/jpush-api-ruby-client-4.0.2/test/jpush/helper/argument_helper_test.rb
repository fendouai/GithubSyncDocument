require 'test_helper'

module JPush
  module Helper
    class ArgumentHelperTest < JPush::Test

      def setup
        @klass = Class.new{ extend ArgumentHelper }
      end

      def test_build_tags
        assert_raises Utils::Exceptions::InvalidArgumentError do
          @klass.build_tags('')
        end
        assert_raises Utils::Exceptions::InvalidArgumentError do
          @klass.build_tags(' ')
        end
        assert_raises Utils::Exceptions::InvalidArgumentError do
          @klass.build_tags([])
        end
        assert_raises Utils::Exceptions::InvalidArgumentError do
          @klass.build_tags(['', ' ', '   ', [], [''], [' '], nil])
        end

        tags = @klass.build_tags(['tag1', 'tag2'])
        assert_instance_of(Array, tags)
        assert_equal 2, tags.length

        tags = @klass.build_tags(['tag1', 'tag2', '', ' ', '   ', [], [''], [' '], nil])
        assert_instance_of(Array, tags)
        assert_equal 2, tags.length

        tags = @klass.build_tags('tag')
        assert_instance_of(Array, tags)
        assert_equal 1, tags.length

        assert_raises Utils::Exceptions::OverLimitError do
          @klass.build_tags(['tag1', 'tag2', 'tag3'], 2)
        end

        tags = @klass.build_tags(['tag1', 'tag2', 'tag3'], 3)
        assert_instance_of(Array, tags)
      end

      def test_build_platform
        @klass.build_platform('android')
        @klass.build_platform(['android', 'ios'])
        assert_raises  Utils::Exceptions::InvalidElementError do
          @klass.build_platform('wp')
        end
      end

    end
  end
end
